export type Gem = {
  name: string;
  level_profit: number;
  level_c_profit: number | null;
  level_q_c_profit: number | null;
  xp_adjusted_level_profit: number;
  xp_adjusted_c_profit: number | null;
  xp_adjusted_q_c_profit: number | null;
  vaal_orb_profit: number | null;
  vaal_orb_20q_profit: number | null;
  vaal_level_profit: number | null;
  gem_type: "normal" | "vaal" | "awakened" | "exceptional" | "transfigured";
  img: string | null;
};
