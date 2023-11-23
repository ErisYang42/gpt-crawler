import { configs } from "../config.js";
import { crawl, write } from "./core.js";

/*
multi configs support only crawl all matched pages once
maxPagesToCrawl and requestQueue seems shared, which will cause problem when crawl different sites with maxPagesToCrawl
*/
for (const config of configs) {
  // log start with config info
  console.log("start crawl config: ", config);
  await crawl(config);
  await write(config);

  // log end with config info
  console.log("end crawl config: ", config);
}