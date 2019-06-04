import * as React from "react";
import Job from "../../components/job/job";
import "./list.css";
import { testData, IJob } from "../../test-data";

export interface IProps {
  filteredList: IJob[];
}

export interface IState {}

class List extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    console.log(testData);
    return (
      <>
        <div className="jobsList">
          <div className="tableHeading">
            <Job job={testData[0]} />
            <hr />
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
