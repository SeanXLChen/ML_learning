import { Button, Card, Col, Container, Row } from "react-bootstrap";
import { PiFlowerTulipDuotone, PiPlantDuotone, PiQuestionDuotone, PiTreeDuotone } from "react-icons/pi";
import { Link } from "react-router-dom";

import { homeCardItems } from "../../static/homeCardItems";
import "../../styles/home.scss";

export default function Home() {
  /**
   * renderIcon -- render an icon based on the icon name
   *
   * @param icon -- the icon name
   * @param iconColor -- the color of the icon
   * @returns -- the icon component
   */
  const renderIcon = (category: string) => {
    switch (category) {
      case "novice":
        return (
          <div className="novice">
            <PiPlantDuotone />
          </div>
        );
      case "intermediate":
        return (
          <div className="intermediate">
            <PiFlowerTulipDuotone />
          </div>
        );
      case "expert":
        return (
          <div className="expert">
            <PiTreeDuotone />
          </div>
        );
      default:
        return (
          <div>
            <PiQuestionDuotone />
          </div>
        )
    }
  };

  return (
    <Container className="container-home">
      <Row xs={1} md={3}>
        {homeCardItems.map((item) => (
          <Col key={item.title}>
            <Card className={`${item.category}-border`}>
              <Card.Body>
                <Card.Title className="card-title-icon">
                  {renderIcon(item.category)}
                </Card.Title>
                <Card.Title>{item.title}</Card.Title>
                <Card.Text>{item.text}</Card.Text>
                <Card.Text>
                  {item.buttons.map((button) => (
                    <Link key={button.path} to={button.path}>
                      <Button variant="outline-dark">{button.text}</Button>
                    </Link>
                  ))}
                </Card.Text>
              </Card.Body>
              <div
                className={`${item.category}-background card-underline `}
              ></div>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}
