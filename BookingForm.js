import React, {
  useState
} from "react";

const BookingForm = ({
  handleBooking
}) => {

  const [name, setName] =
    useState("");

  const [date, setDate] =
    useState("");

  const submitHandler = (e) => {
    e.preventDefault();

    handleBooking({
      name,
      date
    });
  };

  return (
    <form onSubmit={submitHandler}>
      <input
        type="text"
        placeholder="Name"
        onChange={(e) =>
          setName(e.target.value)
        }
      />

      <input
        type="date"
        onChange={(e) =>
          setDate(e.target.value)
        }
      />

      <button>
        Book Appointment
      </button>
    </form>
  );
};

export default BookingForm;