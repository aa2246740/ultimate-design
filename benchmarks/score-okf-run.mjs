#!/usr/bin/env node
import { readFileSync } from "node:fs";

const rubric = JSON.parse(readFileSync(new URL("./okf-rubric.json", import.meta.url), "utf8"));
const inputPath = process.argv[2];

if (!inputPath) {
  console.error("Usage: node benchmarks/score-okf-run.mjs path/to/run-score.json");
  console.error("Input format: { \"scores\": { \"request_integrity\": 12, ... } }");
  process.exit(2);
}

const run = JSON.parse(readFileSync(inputPath, "utf8"));
const scores = run.scores || {};
let total = 0;
const rows = [];

for (const dimension of rubric.dimensions) {
  const raw = Number(scores[dimension.id] ?? 0);
  const score = Math.max(0, Math.min(dimension.points, raw));
  total += score;
  rows.push({
    id: dimension.id,
    label: dimension.label,
    score,
    max: dimension.points,
  });
}

const result = {
  rubric: rubric.name,
  version: rubric.version,
  total,
  max: rubric.total_points,
  percent: Math.round((total / rubric.total_points) * 1000) / 10,
  dimensions: rows,
};

console.log(JSON.stringify(result, null, 2));
process.exit(total > 0 ? 0 : 1);
