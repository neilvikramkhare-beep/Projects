export const BOOK_APPOINTMENT =
  "BOOK_APPOINTMENT";

export const bookAppointment =
  (appointmentData) => {
    return async (dispatch) => {

      setTimeout(() => {

        dispatch({
          type: BOOK_APPOINTMENT,
          payload: appointmentData
        });

        alert(
          `Appointment booked for ${appointmentData.name}`
        );

      }, 1000);
    };
  };