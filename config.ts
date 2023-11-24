import { Config } from "./src/config";

const outputDir = "outputs";
const defaultMaxRequestsPerMinute = 60;
const defaultMaxConcurrency = 10;
const getToday = () => {
  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth() + 1;
  const day = today.getDate();
  return `${year}${month}${day}`;
}
const makeOutputFileName = (name: string) => {
  // file name like: outputs/20210901-nextjs-dev-docs.json
  return `${outputDir}/${getToday()}-${name}.json`;
}

export const defaultConfig: Config = {
  url: "https://www.builder.io/c/docs/developers",
  match: "https://www.builder.io/c/docs/**",
  maxPagesToCrawl: 50,
  outputFileName: "output.json",
};

export const NextjsConfig: Config = {
  url: "https://nextjs.org/docs",
  match: "https://nextjs.org/docs/**",
  maxRequestsPerMinute: defaultMaxRequestsPerMinute,
  maxConcurrency: defaultMaxConcurrency,
  outputFileName: makeOutputFileName("nextjs-dev-docs"),
};

export const OpenAIAPIDocsURLConfig: Config = {
  url: "https://platform.openai.com/docs/introduction",
  match: "https://platform.openai.com/docs/**",
  extractUrlOnly: true,
  maxRequestsPerMinute: defaultMaxRequestsPerMinute,
  maxConcurrency: defaultMaxConcurrency,
  outputFileName: makeOutputFileName("openai-api-docs-urls"),
}

export const configs = [
  NextjsConfig,
  OpenAIAPIDocsURLConfig,
];