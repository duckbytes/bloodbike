import * as React from "react";
import "./header.css";

export interface IProps {}

export interface IState {}

class Header extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    return (
      <>
        <div className="header">
          <span className="logo">Logo</span>
          <h1>
            Co-ordinator <br />
            dashboard
          </h1>
          <div className="commandBox">Command box here</div>
        </div>
      </>
    );
  }
}

export default Header;
