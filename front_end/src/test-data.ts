export interface IJob {
  timeOfCall: string;
  contents: string;
  from: string;
  to: string;
  rider: string;
  collected: number | string;
  delivered: number | string;
}

export const testData: IJob[] = [
  {
    timeOfCall: "TOC",
    contents: "Contents",
    from: "From",
    to: "To",
    rider: "Rider",
    collected: "Collected at",
    delivered: "Delivered at"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "North",
    collected: "1938",
    delivered: "2005"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "2030"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "unassigned",
    collected: "1938",
    delivered: "2005"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "2030"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "North",
    collected: "1938",
    delivered: "2005"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "2030"
  }
];
export default testData;
