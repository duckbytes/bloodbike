import * as React from "react";
import "./job.css";
import { IJob } from "../../test-data";

export interface IProps {
  job: IJob;
}

export interface IState {}

class Job extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    return (
      <>
        <div className="job">
          <div className="packageContents">{this.props.job.contents}</div>
          <div className="transportFrom">{this.props.job.from}</div>
          <div className="transportTo">{this.props.job.to}</div>
          <div className="rider">{this.props.job.rider}</div>
          <div className="timeOfCall">{this.props.job.timeOfCall}</div>
          <div className="collected">{this.props.job.collected}</div>
          <div className="delivered">{this.props.job.delivered}</div>
        </div>
      </>
    );
  }
}

export default Job;
