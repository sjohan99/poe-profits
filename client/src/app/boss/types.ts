type Drop = {
  name: string;
  price: number;
  droprate: number;
  reliable: boolean;
  trade_link: string | null;
  img: string | null;
};

type EntranceItem = {
  name: string;
  price: number;
  quantity: number;
  img: string | null;
};

export type DetailedBossInfo = {
  id: string;
  name: string;
  drops: Drop[];
  entrance_items: EntranceItem[];
};

export type Boss = {
  name: string;
  id: string;
  value: number;
  reliable: boolean;
  img: string | null;
};
