import React from "react";
import Header from "./Header";
import Footer from "./Footer";

const Layout = (porps) => {
  return (
    <div>
      <Header />
      <main>{porps.childeren}</main>
      <Footer />
    </div>
  );
};

export default Layout;
