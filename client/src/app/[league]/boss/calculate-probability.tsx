"use client";

import { useEffect, useState } from "react";
import type { BeginMessage, WorkerSendMessage, Item } from "./types";
import TextInput from "~/components/text-input";
import { ProgressButton } from "~/components/button";
import Tooltip from "~/components/tooltip";

type LoadingState = {
  loading: boolean;
  totalSimulations?: number;
  simulationsDone?: number;
};
export default function CalculateProbability(params: { items: Item[] }) {
  const { items } = params;
  const [profitProbability, setProfitProbability] = useState<number | null>(
    null,
  );

  const defaultKills = 100;
  const defaultSimulations = 10000;

  const [kills, setKills] = useState(defaultKills);
  const [simulations, setSimulations] = useState(defaultSimulations);
  const [loading, setLoading] = useState<LoadingState>({
    loading: false,
  });

  useEffect(() => {
    setProfitProbability(null);
  }, [kills, simulations]);

  const handleCalculate = () => {
    if (loading.loading) {
      return;
    }

    setLoading({
      loading: true,
      simulationsDone: 0,
      totalSimulations: simulations,
    });

    const worker = new Worker(new URL("./calculateWorker.js", import.meta.url));
    worker.postMessage({
      items,
      kills,
      simulations: simulations,
    } satisfies BeginMessage);

    worker.onmessage = (e: MessageEvent<WorkerSendMessage>) => {
      if (e.data.type === "in-progress") {
        setLoading({
          loading: true,
          simulationsDone: e.data.simulationsDone,
          totalSimulations: e.data.simulationsTotal,
        });
        return;
      }
      if (e.data.type === "done") {
        setProfitProbability(e.data.probability);
        setLoading({ loading: false });
        worker.terminate();
      }
    };
  };

  return (
    <div className="responsive-text-s flex flex-col gap-2 sm:max-w-lg">
      <h3>Calculate the probability of making profit after X kills:</h3>
      <div className="flex flex-col gap-2">
        <div className="flex flex-row items-center justify-between gap-2">
          <p>Number of kills:</p>
          <div className="w-28">
            <TextInput
              restriction="number"
              placeholderText={defaultKills.toString()}
              inputCallback={function (text: string): void {
                if (text === "") {
                  setKills(defaultKills);
                  return;
                }
                setKills(parseInt(text));
              }}
            ></TextInput>
          </div>
        </div>
        <div className="flex flex-row items-center justify-between gap-2">
          <div className="flex flex-row gap-2">
            <p>Accuracy:</p>
            <Tooltip icon="question">
              <p>Higher = slower but more accurate</p>
            </Tooltip>
          </div>
          <select
            className="h-10 w-28 rounded border border-accent-2 bg-transparent p-1"
            value={10000}
            onChange={(e) => setSimulations(parseInt(e.target.value))}
          >
            <option className="bg-accent-1" value={1000}>
              low
            </option>
            <option className="bg-accent-1" value={5000}>
              medium
            </option>
            <option className="bg-accent-1" value={10000}>
              high
            </option>
            <option className="bg-accent-1" value={25000}>
              very high
            </option>
          </select>
        </div>
        <ProgressButton
          onClick={handleCalculate}
          disabled={loading.loading}
          progress={
            loading.loading
              ? loading.simulationsDone! / loading.totalSimulations!
              : 0
          }
        >
          {loading.loading ? "Running Simulations" : "Start Simulation"}
        </ProgressButton>
        {profitProbability === null ? null : (
          <div className="flex flex-row items-center justify-between">
            <p>Probability to profit after {kills} kills:</p>
            <p className="font-bold">{(100 * profitProbability).toFixed(2)}%</p>
          </div>
        )}
      </div>
    </div>
  );
}
