import {
  BOOK_APPOINTMENT
} from "../actions/appointmentActions";

const initialState = {
  appointments: []
};

const appointmentReducer = (
  state = initialState,
  action
) => {
  switch (action.type) {
    case BOOK_APPOINTMENT:
      return {
        appointments: [
          ...state.appointments,
          action.payload
        ]
      };

    default:
      return state;
  }
};

export default appointmentReducer;