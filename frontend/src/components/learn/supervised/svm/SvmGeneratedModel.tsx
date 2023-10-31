import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Card, Form, Button } from "react-bootstrap";

import ConfusionMatrix from "../../../../smallcomponents/ConfusionMatrix";
import AssessmentMetrics from "../../../../smallcomponents/AssessmentMetrics";
import { svmPlotTypes } from "../../../../static/svmPlotTypes";
import InteractiveHelper from "../../../helper/interactiveHelper";
import helperContentText from "../../../../static/helperContentText.json";
import "../../../../styles/svm.scss";

export default function SvmGeneratedModel() {
  const [trainingResults, setTrainingResults] = useState<any>(null);
  const [parameters, setParameters] = useState<any>(null);
  const [plotType, setPlotType] = useState<string>("");
  const [confusionMatrix, setConfusionMatrix] = useState<any>(null);

  const trainSVMModel = async (params: any) => {
    try {
      const request = {
        dataset_name: params.dataset,
        svm_params: {
          C: params.C,
          kernel: params.kernel,
          degree: params.degree,
          gamma: params.gamma,
          coef0: params.coef0,
        },
        train_size: params.trainSize,
        k_folds: params.kFolds,
        selected_features: params.features,
      };
      console.log(JSON.stringify(request));

      const headers = {
        "Content-Type": "application/json",
      };

      await axios
        .post("http://127.0.0.1:5000/train_svm", request, {
          headers: headers,
        })
        .then((response) => {
          console.log(response);
          setTrainingResults(response);
          setConfusionMatrix(
            JSON.parse(response.data.all_results[0].confusion_matrix_plot_json)
          );
          // Save response to local storage
          localStorage.setItem("svm-results", JSON.stringify(response));
        });

      // Currently, the API is not returning the plot data.
      // await axios
      //   .post("http://127.0.0.1:5000/select_plot", { plot_type: "histogram" })
      //   .then((response) => {
      //     console.log("select plot: ", response);
      //   });

      // await axios.post("http://127.0.0.1:5000/plot").then((response) => {
      //   console.log("plot: ", response);
      // });
    } catch (error) {
      console.error("Error while making the API call:", error);
    }
  };

  const handleSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = event.target;
    setPlotType(value);
  };

  useEffect(() => {
    const SVM = localStorage.getItem("train-svm");
    const parsedParameters = SVM ? JSON.parse(SVM) : null;
    console.log("parameters: ", parsedParameters);
    setParameters(parsedParameters);
    trainSVMModel(parsedParameters);
  }, []);

  return (
    <div className="generatedModel">
      {trainingResults && (
        <div className="generated-model-container">
          <div className="measures-card">
            <div className="measures-container p-0">
              <Card className="assessment-metrics-card">
                <Card.Header>Assessment Metrics</Card.Header>
                <Card.Body>
                  <AssessmentMetrics
                    precision={trainingResults?.data.all_results[0].precision.toFixed(
                      3
                    )}
                    recall={trainingResults?.data.all_results[0].recall.toFixed(
                      3
                    )}
                    f1={trainingResults?.data.all_results[0].f1_score.toFixed(
                      3
                    )}
                    accuracy={trainingResults?.data.all_results[0].accuracy.toFixed(
                      3
                    )}
                  />
                </Card.Body>
              </Card>
              {confusionMatrix && (
                <Card className="confusion-matrix-card">
                  <Card.Header>Confusion Matrix</Card.Header>
                  <Card.Body>
                    <ConfusionMatrix
                      truePositive={confusionMatrix.data[0].z[0][0].toFixed(3)}
                      falsePositive={confusionMatrix.data[0].z[0][1].toFixed(3)}
                      falseNegative={confusionMatrix.data[0].z[1][0].toFixed(3)}
                      trueNegative={confusionMatrix.data[0].z[1][1].toFixed(3)}
                    />
                  </Card.Body>
                </Card>
              )}
            </div>
          </div>
          <Card className="graph-card">
            <Card.Header>Graphs</Card.Header>
            <Card.Body>
              <Card className="plot-type-card">
                <Card.Body>
                  <div className="graph">
                    <img src="https://via.placeholder.com/150" alt="graph 1" />
                  </div>
                </Card.Body>
              </Card>
            </Card.Body>
          </Card>
        </div>
      )}
      <Link className="mx-auto" to="/learn/supervised/svm/train-model">
        <Button type="button">Back to Train Model</Button>
      </Link>
      <InteractiveHelper section={helperContentText.svm} />
    </div>
  );
}
