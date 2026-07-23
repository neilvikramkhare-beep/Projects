import { combineReducers } from "redux";

import serviceReducer
from "./serviceReducer";

import appointmentReducer
from "./appointmentReducer";

const rootReducer =
  combineReducers({
    serviceState: serviceReducer,
    appointmentState: appointmentReducer
  });

export default rootReducer;