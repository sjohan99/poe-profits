import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";

export const env = createEnv({
  /**
   * Specify your server-side environment variables schema here. This way you can ensure the app
   * isn't built with invalid env vars.
   */
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]),
    RATE_LIMIT_TOKEN_REFILL_RATE_MS: z.number({ coerce: true }),
    RATE_LIMIT_TOKEN_BUCKET_CAPACITY: z.number({ coerce: true }),
    ISR_REVALIDATE_SECONDS: z.number({ coerce: true }),
    SITE_URL: z.string(),
  },

  /**
   * Specify your client-side environment variables schema here. This way you can ensure the app
   * isn't built with invalid env vars. To expose them to the client, prefix them with
   * `NEXT_PUBLIC_`.
   */
  client: {
    // NEXT_PUBLIC_CLIENTVAR: z.string(),
    NEXT_PUBLIC_API_HOST: z.string(),
    NEXT_PUBLIC_CACHE_FETCH_SECONDS: z.number({ coerce: true }),
  },

  /**
   * You can't destruct `process.env` as a regular object in the Next.js edge runtimes (e.g.
   * middlewares) or client-side so we need to destruct manually.
   */
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    RATE_LIMIT_TOKEN_REFILL_RATE_MS:
      process.env.RATE_LIMIT_TOKEN_REFILL_RATE_MS,
    RATE_LIMIT_TOKEN_BUCKET_CAPACITY:
      process.env.RATE_LIMIT_TOKEN_BUCKET_CAPACITY,
    ISR_REVALIDATE_SECONDS: process.env.ISR_REVALIDATE_SECONDS,
    NEXT_PUBLIC_API_HOST: process.env.NEXT_PUBLIC_API_HOST,
    NEXT_PUBLIC_CACHE_FETCH_SECONDS:
      process.env.NEXT_PUBLIC_CACHE_FETCH_SECONDS,
    SITE_URL: process.env.SITE_URL,
  },
  /**
   * Run `build` or `dev` with `SKIP_ENV_VALIDATION` to skip env validation. This is especially
   * useful for Docker builds.
   */
  skipValidation: !!process.env.SKIP_ENV_VALIDATION,
  /**
   * Makes it so that empty strings are treated as undefined. `SOME_VAR: z.string()` and
   * `SOME_VAR=''` will throw an error.
   */
  emptyStringAsUndefined: true,
});
