export const FETCH_SERVICES_REQUEST =
  "FETCH_SERVICES_REQUEST";

export const FETCH_SERVICES_SUCCESS =
  "FETCH_SERVICES_SUCCESS";

export const fetchServices = () => {
  return async (dispatch) => {
    dispatch({
      type: FETCH_SERVICES_REQUEST
    });

    const services = [
      {
        id: 1,
        title: "Root Canal",
        description:
          "Root canal saves damaged teeth."
      },
      {
        id: 2,
        title: "Dental Fillings",
        description:
          "Repairs cavities and fractures."
      },
      {
        id: 3,
        title: "Dental Implants",
        description:
          "Permanent replacement teeth."
      }
    ];

    setTimeout(() => {
      dispatch({
        type: FETCH_SERVICES_SUCCESS,
        payload: services
      });
    }, 1000);
  };
};