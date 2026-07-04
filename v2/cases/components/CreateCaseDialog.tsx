import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { Plus } from "lucide-react";

import api from "../../../api/client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

export default function CreateCaseDialog() {
  const qc = useQueryClient();

  const [open, setOpen] = useState(false);

  const [title, setTitle] = useState("");
  const [caseNumber, setCaseNumber] = useState("");
  const [court, setCourt] = useState("");
  const [description, setDescription] = useState("");

const [cnr, setCnr] = useState("");
const [captcha, setCaptcha] = useState("");
const [sessionId, setSessionId] = useState("");
const [captchaUrl, setCaptchaUrl] = useState("");
const [loadingCaptcha, setLoadingCaptcha] = useState(false);
const [importing, setImporting] = useState(false);

  const mutation = useMutation({
    mutationFn: async () => {
      const res = await api.post("/cases/", {
        title,
        case_number: caseNumber,
        court,
        description,
      });

      return res.data;
    },

    onSuccess: () => {
      qc.invalidateQueries({
        queryKey: ["cases"],
      });

      setTitle("");
      setCaseNumber("");
      setCourt("");
      setDescription("");

      setOpen(false);
    },
  });

  
async function fetchCaptcha() {
  setLoadingCaptcha(true);

  try {
    const response = await api.get("/court/captcha", {
      responseType: "blob",
    });

    const sid = response.headers["x-session-id"];

    if (!sid) {
      throw new Error("Missing x-session-id header");
    }

    setSessionId(sid);
    setCaptchaUrl(URL.createObjectURL(response.data));
  } finally {
    setLoadingCaptcha(false);
  }
}

async function importFromECourts() {
  if (!sessionId) {
    alert("Load CAPTCHA first.");
    return;
  }

  setImporting(true);

  try {
    const { data } = await api.post("/court/search", {
      cnr,
      captcha,
      session_id: sessionId,
    });

    console.log(data);

    if (data.success) {
      alert("Case imported successfully.");
      qc.invalidateQueries({ queryKey: ["cases"] });
      setOpen(false);
    } else {
      alert(data.message || "Search failed.");
      await fetchCaptcha();
      setCaptcha("");
    }
  } finally {
    setImporting(false);
  }
}

function submit(e: React.FormEvent) {
    e.preventDefault();
    mutation.mutate();
  }

  return (
    <Dialog
      open={open}
      onOpenChange={setOpen}
    >
      <DialogTrigger asChild>
        <Button>
          <Plus className="mr-2 h-4 w-4" />
          New Case
        </Button>
      </DialogTrigger>

      
      <DialogContent className="sm:max-w-xl">
        <DialogHeader>
          <DialogTitle>Import Case from eCourts</DialogTitle>
        </DialogHeader>

        <div className="space-y-4">

          <div>
            <Label>CNR Number</Label>
            <Input
              value={cnr}
              onChange={(e)=>setCnr(e.target.value)}
              placeholder="MHCC010142422024"
            />
          </div>

          <Button
            type="button"
            onClick={fetchCaptcha}
            disabled={loadingCaptcha}
            className="w-full"
          >
            {loadingCaptcha ? "Loading CAPTCHA..." : "Get CAPTCHA"}
          </Button>

          {captchaUrl && (
            <img
              src={captchaUrl}
              alt="CAPTCHA"
              className="w-40 rounded border"
            />
          )}

          <div>
            <Label>CAPTCHA</Label>
            <Input
              value={captcha}
              onChange={(e)=>setCaptcha(e.target.value)}
              placeholder="Enter CAPTCHA"
            />
          </div>

          <Button
            type="button"
            onClick={importFromECourts}
            disabled={importing}
            className="w-full"
          >
            {importing ? "Searching..." : "Import from eCourts"}
          </Button>

        </div>
      </DialogContent>

    </Dialog>
  );
}
