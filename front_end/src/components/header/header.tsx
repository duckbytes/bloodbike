import * as React from "react";
import "./header.css";
import logo from "./logo.png";

export interface IProps {}

export interface IState {}

class Header extends React.Component<IProps, IState> {
  // state = { :  }
  public render() {
    return (
      <>
        <div className="header">
          <img src={logo} alt={"charity logo"} className="logo" />
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
