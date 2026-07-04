import { useState } from "react";
import api from "../../../api/client";

import { Button } from "@/components/ui/button";
import { Dialog,DialogContent,DialogHeader,DialogTitle,DialogTrigger } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function ImportECourtsDialog() {
  const [open,setOpen]=useState(false);
  const [sessionId,setSessionId]=useState("");
  const [cnr,setCnr]=useState("");
  const [captcha,setCaptcha]=useState("");
  const [captchaUrl,setCaptchaUrl]=useState("");
  const [result,setResult]=useState<any>(null);
  const [loading,setLoading]=useState(false);

  
  async function getCaptcha(){
    setResult(null);

    const r = await api.get("/court/captcha", {
      responseType: "blob",
    });

    const sid = r.headers["x-session-id"];

    if (!sid) {
      throw new Error("Missing x-session-id");
    }

    setSessionId(sid);

    if (captchaUrl) {
      URL.revokeObjectURL(captchaUrl);
    }

    setCaptchaUrl(URL.createObjectURL(r.data));
  }


  async function search(){
    setLoading(true);

    try{
      const r=await api.post("/court/search-by-cnr",{
        session_id:sessionId,
        cnr,
        captcha,
      });

      setResult(r.data);
    }finally{
      setLoading(false);
    }
  }

  return(
    <Dialog open={open} onOpenChange={setOpen}>

      <DialogTrigger asChild>
        <Button variant="secondary">
          Import from eCourts
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-2xl">

        <DialogHeader>
          <DialogTitle>Import from eCourts</DialogTitle>
        </DialogHeader>

        <div className="space-y-4">

          <div>
            <Label>CNR Number</Label>
            <Input
              value={cnr}
              onChange={e=>setCnr(e.target.value.toUpperCase())}
            />
          </div>

          <Button onClick={getCaptcha}>
            Get CAPTCHA
          </Button>

          {captchaUrl && (
            <>
              <img
                src={captchaUrl}
                alt="captcha"
                className="rounded border"
              />

              <Input
                placeholder="Enter CAPTCHA"
                value={captcha}
                onChange={e=>setCaptcha(e.target.value)}
              />

              <Button
                onClick={search}
                disabled={loading}
              >
                {loading ? "Searching..." : "Search"}
              </Button>
            </>
          )}

          {result && (
            <pre className="max-h-96 overflow-auto rounded bg-muted p-4 text-xs">
{JSON.stringify(result,null,2)}
            </pre>
          )}

        </div>

      </DialogContent>

    </Dialog>
  );
}
