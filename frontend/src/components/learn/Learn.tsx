import { Button, Card, Col, Container, Row } from "react-bootstrap";
import { PiQuestionDuotone } from "react-icons/pi";
import { Link } from "react-router-dom";

import { learnCardItems } from "../../static/learnCardItems";
import "../../styles/learn.scss";

const algorithm_types = [
  "Supervised Learning",
  "Unsupervised Learning",
  "Reinforcement Learning",
  "Deep Learning",
];

export default function Learn() {
  return (
    <Container>
      {algorithm_types.map((type) => (
        <Container className="container-learn">
          <Row key={type}>
            <h2 className="ml-type">{type}</h2>
          </Row>
          <Row xs={1} md={2} xl={3}>
            {learnCardItems
              .filter((item) => item.category === type)
              .map((item) => (
                <Col key={item.title}>
                  <Card className="algo-card-classical">
                    <Card.Body>
                      <Row className="row-info">
                        <Col className="col-image">
                          <Card.Title className="algo-card-title-icon">
                            <PiQuestionDuotone />
                          </Card.Title>
                        </Col>
                        <Col className="col-content">
                          <Card.Title>{item.title}</Card.Title>
                          <Card.Text>{item.text}</Card.Text>
                        </Col>
                      </Row>
                      <Row className="row-button">
                        {item.buttons.map((button) => (
                          <Col key={button.text}>
                            <Link key={button.path} to={button.path}>
                              <Button variant="outline-dark">
                                {button.text}
                              </Button>
                            </Link>
                          </Col>
                        ))}
                      </Row>
                    </Card.Body>
                  </Card>
                </Col>
              ))}
          </Row>
        </Container>
      ))}
    </Container>
  );
}
