import * as React from "react";
import "./job.css";

export interface IProps {}

export interface IState {}

class Job extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    return (
      <>
        <div className="job">The quick brown fox jumps over the lazy dog.</div>
      </>
    );
  }
}

export default Job;
