import React from 'react'
import { Table } from 'react-bootstrap';
import '../styles/assessmentMetrics.scss';

interface AssessmentMetricsProps {
    precision: number;
    recall: number;
    f1: number;
    accuracy: number;
  }

export default function AssessmentMetrics(props: AssessmentMetricsProps) {
  return (
    <div className="assessment-metrics-container">
        <Table bordered hover>
            <thead>
                <tr>
                    <th colSpan={2}>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>Precision</th>
                    <td>{props.precision}</td>
                </tr>
                <tr>
                    <th>Recall</th>
                    <td>{props.recall}</td>
                </tr>
                <tr>
                    <th>F1</th>
                    <td>{props.f1}</td>
                </tr>
                <tr>
                    <th>Accuracy</th>
                    <td>{props.accuracy}</td>
                </tr>
            </tbody>
        </Table>
    </div>
  )
}
