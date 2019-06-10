import * as React from "react";
import Job from "../../components/job/job";
import "./list.css";
import { IJob } from "../../test-data";

export interface IProps {
  filteredList: IJob[];
}

export interface IState {}

class List extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    return (
      <>
        <div className="jobsList">
          <div className="tableHeading">
            {/* <Job job={testData[0]} /> */}
            {/* if you re-arrange columns in Job component, you need to re-arrange these, too */}
            <div>
              <div>Contents</div>
              <div>From</div>
              <div>To</div>
              <div>Rider</div>
              <div>TOC</div>
              <div>Collected at</div>
              <div>Delivered at</div>
            </div>
          </div>
          {this.props.filteredList.map((jobdata, index) => (
            <Job key={index} job={jobdata} />
          ))}
        </div>
      </>
    );
  }
}

export default List;
