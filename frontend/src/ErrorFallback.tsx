export default function ErrorFallback({ error }: { error: Error }) {
  return (
    <div style={{ padding: 20, color: "red", whiteSpace: "pre-wrap" }}>
      <h1>React Runtime Error</h1>
      <pre>{error.stack}</pre>
    </div>
  );
}
