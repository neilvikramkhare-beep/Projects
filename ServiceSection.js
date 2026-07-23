import ServiceCard from "./ServiceCard";

const ServiceSection = ({ services }) => {
  return (
    <div>
      <h2>Our Services</h2>

      {services.map((service) => (
        <ServiceCard
          key={service.id}
          title={service.title}
          description={
            service.description
          }
        />
      ))}
    </div>
  );
};

export default ServiceSection;