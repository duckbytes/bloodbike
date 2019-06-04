import * as React from "react";
import Job from "../../components/job/job";
import "./list.css";
import { testData } from "../../test-data";

export interface IProps {}

export interface IState {}

class List extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    console.log(testData);
    return (
      <>
        <div className="jobsList">
          <div className="tableHeading">
            <Job />
            <hr />
          </div>
          <Job />
          <Job />
          <Job />
          <Job />
          <Job />
        </div>
      </>
    );
  }
}

export default List;
