import React, { Component } from "react";
import "./App.css";
import Header from "./components/header/header";
import List from "./containers/list/list";

class App extends Component {
  public render() {
    return (
      <>
        <Header />
        <List />
      </>
    );
  }
}

export default App;
