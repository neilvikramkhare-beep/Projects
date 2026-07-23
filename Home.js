import ServiceSection
from "./ServiceSection";

import AppointmentSection
from "./AppointmentSection";

const Home = ({
  services,
  handleBooking
}) => {

  return (
    <>
      <ServiceSection
        services={services}
      />

      <AppointmentSection
        handleBooking={
          handleBooking
        }
      />
    </>
  );
};

export default Home;