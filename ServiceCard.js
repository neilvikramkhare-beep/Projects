const ServiceCard = ({
  title,
  description
}) => {
  return (
    <div className="card p-3 mb-3">
      <h4>{title}</h4>
      <p>{description}</p>
    </div>
  );
};

export default ServiceCard;