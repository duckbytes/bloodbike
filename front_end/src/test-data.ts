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
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "unassigned",
    collected: "1938",
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "North",
    collected: "not yet",
    delivered: "not yet"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "en route"
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
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "unassigned",
    collected: "1938",
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "en route"
  },
  {
    timeOfCall: "1907",
    contents: "blood",
    from: "Eliz.Casson unit",
    to: "BRI A&E",
    rider: "North",
    collected: "not yet",
    delivered: "not yet"
  },
  {
    timeOfCall: "1907",
    contents: "milk",
    from: "SoutmeadNICU",
    to: "Weston Handover",
    rider: "West",
    collected: "1940",
    delivered: "en route"
  }
];
export default testData;
