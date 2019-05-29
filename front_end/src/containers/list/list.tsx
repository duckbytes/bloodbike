import * as React from "react";
import Job from "../../components/job/job";
import "./list.css";

export interface IProps {}

export interface IState {}

class List extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
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
