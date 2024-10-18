export type Item = {
  name: string;
  chaos_value: number;
  icon: string | null;
  reroll_weight: number;
  expected_reroll_profit: number;
  lifeforce_per_reroll: number;
};

export type Lifeforce = {
  name: string;
  chaos_value: number;
  icon: string | null;
};
