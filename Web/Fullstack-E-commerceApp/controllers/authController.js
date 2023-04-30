import JWT from "jsonwebtoken";
import { comparePassword, hashPassword } from "../helpers/authHelper.js";
import User from "../models/User.js";

// POST REGISTER
export const registerController = async (req, res) => {
  try {
    const { name, email, password, phone, address } = req.body;

    // validation
    if (!name) {
      return res.send({ error: "Name is required!" });
    }
    if (!email) {
      return res.send({ error: "email is required!" });
    }
    if (!password) {
      return res.send({ error: "password is required!" });
    }
    if (!phone) {
      return res.send({ error: "phone is required!" });
    }
    if (!address) {
      return res.send({ error: "address is required!" });
    }

    // check user
    const existingUser = await User.findOne({ email });
    // existing user
    if (existingUser) {
      return res.status(200).send({
        success: true,
        message: "Already Register please login!",
      });
    }
    // register user
    const hashedPassword = await hashPassword(password);
    // save
    const user = new User({
      name,
      email,
      phone,
      address,
      password: hashedPassword,
    }).save();
    res.status(201).send({
      success: true,
      message: "User Register Successfully",
      user,
    });
  } catch (error) {
    console.log(error);
    res.status(500).send({
      success: false,
      message: "Error in Registeration",
      error,
    });
  }
};

// POST LOGIN
export const loginController = async (req, res) => {
  try {
    const { email, password } = req.body;

    // validation
    if (!email || !password) {
      return res.send({ error: "Invalid email or password" });
    }

    // check user
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(200).send({
        success: true,
        message: "Email is not registered",
      });
    }
    // register user
    const match = await comparePassword(password, user.password);
    if (!match) {
      return res.status(200).send({
        success: true,
        message: "Invalid password",
      });
    }
    // token
    const token = await JWT.sign({ _id: user._id }, process.env.JWT_SECRET, {
      expiresIn: "7d",
    });
    return res.status(200).send({
      success: true,
      message: "Login successfully",
      user: {
        name: user.name,
        email: user.email,
        phone: user.phone,
        address: user.address,
      },
      token,
    });
  } catch (error) {
    console.log(error);
    res.status(500).send({
      success: false,
      message: "Error in Login",
      error,
    });
  }
};

export const testController = async (req, res) => {
  try {
    res.send("protected Routes");
  } catch (error) {
    console.log(error);
    res.send({ error });
  }
};
