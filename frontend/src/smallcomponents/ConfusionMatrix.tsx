import React from "react";
import Table from "react-bootstrap/Table";
import "../styles/confusionMatrix.scss";

interface ConfusionMatrixProps {
  truePositive: number;
  trueNegative: number;
  falsePositive: number;
  falseNegative: number;
}

export default function ConfusionMatrix(props: ConfusionMatrixProps) {
  return (
    <div className="confusion-matrix-container">
      <Table bordered hover>
        <thead>
          <tr>
            <th></th>
            <th>Actual True</th>
            <th>Actual False</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th>Predicted True</th>
            <td>{props.truePositive}</td>
            <td>{props.falsePositive}</td>
          </tr>
          <tr>
            <th>Predicted False</th>
            <td>{props.falseNegative}</td>
            <td>{props.trueNegative}</td>
          </tr>
        </tbody>
      </Table>
    </div>
  );
}
