export interface IJob {
  timeOfCall: string;
  contents: string;
  from: string;
  // to: string;
  // rider: "North" | "West" | "East" | "Relief";
  // collected: number | "not colleced";
  // delivered: number | "en route"
}

export const testData: IJob[] = [
  {
    timeOfCall: "TOC",
    contents: "Contents",
    from: "From"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU"
  }
];
export default testData;
