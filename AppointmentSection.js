import BookingForm
from "./BookingForm";

const AppointmentSection = ({
  handleBooking
}) => {
  return (
    <div>
      <h2>
        Book Appointment
      </h2>

      <BookingForm
        handleBooking={
          handleBooking
        }
      />
    </div>
  );
};

export default AppointmentSection;