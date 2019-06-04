export interface IJob {
  timeOfCall: number;
  contents: string;
  from: string;
  // to: string;
  // rider: "North" | "West" | "East" | "Relief";
  // collected: number | "not colleced";
  // delivered: number | "en route"
}

export const testData: IJob[] = [
  {
    timeOfCall: 1907,
    contents: "string",
    from: "string"
  },
  {
    timeOfCall: 1907,
    contents: "string",
    from: "string"
  },
  {
    timeOfCall: 1907,
    contents: "string",
    from: "string"
  }
];
export default testData;
