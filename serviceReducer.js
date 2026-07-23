import {
  FETCH_SERVICES_REQUEST,
  FETCH_SERVICES_SUCCESS
} from "../actions/serviceActions";

const initialState = {
  loading: false,
  services: []
};

const serviceReducer = (
  state = initialState,
  action
) => {
  switch (action.type) {
    case FETCH_SERVICES_REQUEST:
      return {
        ...state,
        loading: true
      };

    case FETCH_SERVICES_SUCCESS:
      return {
        loading: false,
        services: action.payload
      };

    default:
      return state;
  }
};

export default serviceReducer;