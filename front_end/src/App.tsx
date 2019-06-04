import React, { Component } from "react";
import "./App.css";
import Header from "./components/header/header";
import List from "./containers/list/list";
import testData, { IJob } from "./test-data";

export interface IProps {
  filteredList: IJob[];
}

class App extends Component {
  public state = { filteredList: testData };
  public render() {
    return (
      <>
        <Header />
        <List filteredList={this.state.filteredList} />
      </>
    );
  }
}

export default App;
