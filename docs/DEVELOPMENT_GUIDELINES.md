# DEVELOPMENT GUIDELINES
1.  **Isolation:** Do not import scripts from other hazard folders.
2.  **Shared Tools:** Only use cross-cutting utilities found in `shared/`.
3.  **No Legacy Code:** All legacy `ml_engine/` processing pipelines have been destroyed. Do not restore them.
4.  **Hardware:** Adhere strictly to the VRAM limits defined during benchmark testing (e.g., RTX 3050 4GB).
