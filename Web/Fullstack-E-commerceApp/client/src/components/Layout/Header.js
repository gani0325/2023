import React from "react";
import { NavLink } from "react-router-dom";

const Header = () => {
  return (
    <>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarTogglerDemo01"
            aria-controls="navbarTogglerDemo01"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
            <NavLink to="/" class="navbar-brand" href="#">
              Hidden brand
            </NavLink>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <NavLink to="/" class="nav-link ">
                  Home
                </NavLink>
              </li>
              <li class="nav-item">
                <NavLink to="/category" class="nav-link ">
                  Category
                </NavLink>
              </li>
              <li class="nav-item">
                <NavLink to="/register" class="nav-link" href="#">
                  Register
                </NavLink>
              </li>
              <li class="nav-item">
                <NavLink to="/login" class="nav-link" href="#">
                  Login
                </NavLink>
              </li>
              <li class="nav-item">
                <NavLink to="/cart" class="nav-link" href="#">
                  Cart (0)
                </NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Header;
