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
  short_name: string;
  drops: Drop[];
  entrance_items: EntranceItem[];
};

export type Item = {
  name: string;
  price: number;
  droprate: number | null;
  value: number;
  reliable: boolean;
  trade_link: string | null;
  img: string | null;
  type: "drop" | "entrance";
  share?: number;
  quantity?: number;
};

export type Boss = {
  name: string;
  short_name: string;
  id: string;
  value: number;
  reliable: boolean;
  img: string | null;
};

export type DoneMessage = {
  type: "done";
  probability: number;
};

export type InProgressMessage = {
  type: "in-progress";
  simulationsDone: number;
  simulationsTotal: number;
};

export type WorkerSendMessage = DoneMessage | InProgressMessage;

export type BeginMessage = {
  items: Item[];
  kills: number;
  simulations: number;
};
