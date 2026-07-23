const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const authRoutes = require("./routes/authRoutes");
const customerRoutes = require("./routes/customerRoutes");
const accountRoutes = require("./routes/accountRoutes");
const transactionRoutes = require("./routes/transactionRoutes");

const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

app.use("/api/auth", authRoutes);
app.use("/api/customers", customerRoutes);
app.use("/api/accounts", accountRoutes);
app.use("/api/transactions", transactionRoutes);

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
const mongoose = require("mongoose");

const customerSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    address: String,
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("Customer", customerSchema);
const mongoose = require("mongoose");

const accountSchema = new mongoose.Schema({
    customerId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Customer"
    },
    accountNumber: String,
    balance: {
        type: Number,
        default: 0
    },
    accountType: String
});

module.exports = mongoose.model("Account", accountSchema);
const mongoose = require("mongoose");

const transactionSchema = new mongoose.Schema({
    accountId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Account"
    },
    type: String,
    amount: Number,
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("Transaction", transactionSchema);
const express = require("express");
const router = express.Router();
const Customer = require("../models/Customer");

router.post("/", async (req, res) => {
    const customer = await Customer.create(req.body);
    res.json(customer);
});

router.get("/", async (req, res) => {
    const customers = await Customer.find();
    res.json(customers);
});

router.get("/:id", async (req, res) => {
    const customer = await Customer.findById(req.params.id);
    res.json(customer);
});

router.put("/:id", async (req, res) => {
    const customer = await Customer.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
    );

    res.json(customer);
});

router.delete("/:id", async (req, res) => {
    await Customer.findByIdAndDelete(req.params.id);
    res.json({ message: "Deleted" });
});

module.exports = router;
import { configureStore } from "@reduxjs/toolkit";
import customerReducer from "./customerSlice";

export const store = configureStore({
    reducer: {
        customers: customerReducer
    }
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
import { createSlice } from "@reduxjs/toolkit";

const customerSlice = createSlice({
    name: "customers",
    initialState: {
        customers: []
    },
    reducers: {
        setCustomers: (state, action) => {
            state.customers = action.payload;
        }
    }
});

export const { setCustomers } = customerSlice.actions;
export default customerSlice.reducer;
import axios from "axios";

export default axios.create({
    baseURL: "http://10.0.2.2:5000/api"
});
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import LoginScreen from "../screens/LoginScreen";
import DashboardScreen from "../screens/DashboardScreen";
import CustomerScreen from "../screens/CustomerScreen";

const Stack = createNativeStackNavigator();

export default function AppNavigator() {
    return (
        <Stack.Navigator>
            <Stack.Screen name="Login" component={LoginScreen}/>
            <Stack.Screen name="Dashboard" component={DashboardScreen}/>
            <Stack.Screen name="Customers" component={CustomerScreen}/>
        </Stack.Navigator>
    );
}
import React from "react";
import { View, Text } from "react-native";

export default function DashboardScreen() {
    return (
        <View>
            <Text>Total Balance: ₹5,00,000</Text>
            <Text>Accounts: 15</Text>
            <Text>Transactions Today: 53</Text>
        </View>
    );
}
import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import api from "../api/api";

export default function CustomerScreen() {

    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        loadCustomers();
    }, []);

    const loadCustomers = async () => {
        const response = await api.get("/customers");
        setCustomers(response.data);
    };

    return (
        <FlatList
            data={customers}
            renderItem={({ item }) => (
                <View>
                    <Text>{item.name}</Text>
                    <Text>{item.email}</Text>
                </View>
            )}
        />
    );
}
router.post("/login", async (req, res) => {

    const token = jwt.sign(
        { userId: user._id },
        process.env.JWT_SECRET,
        { expiresIn: "1d" }
    );

    res.json({
        token
    });
});
