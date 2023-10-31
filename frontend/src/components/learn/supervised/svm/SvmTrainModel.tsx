import axios from "axios";
import { useEffect, useState } from "react";
import { Button, Card, Form } from "react-bootstrap";
import { Link } from "react-router-dom";

import InteractiveHelper from "../../../helper/interactiveHelper";
import helperContentText from "../../../../static/helperContentText.json";
import { svmDataSetNames } from "../../../../static/svmDataSetNames";
import "../../../../styles/svm.scss";

// SVM Parameters:
// C: regularization parameter
// kernel: "linear", "poly", "rbf", "sigmoid", "precomputed"
// degree: only used for poly and is ignored by all other kernels
// coef0: only significant for poly and sigmoid
// gamma: only used for rbf, poly, and sigmoid
// trainSize: percentage of data to use for training
// k_folds: number of folds for cross validation

interface SvmParameters {
  dataset: string;
  kernel: string;
  C: number;
  cLog: number;
  gamma: number;
  gammaLog: number;
  coef0: number;
  degree: number;
  trainSize: number | null;
  kFolds: number | null;
  technique: string;
  features: { [key: string]: boolean };
}

export default function SvmTrainModel() {
  // dummy feature list (to be updated with API call)
  const defaultFeatures = {
    "dummy feature 1": true,
    "dummy feature 2": true,
    "dummy feature 3": true,
    "dummy feature 4": true,
    "dummy feature 5": true,
    "dummy feature 6": true,
    "dummy feature 7": true,
    "dummy feature 8": true,
    "dummy feature 9": true,
    "dummy feature 10": true,
  };

  // set initial state
  const defaultParameters: SvmParameters = {
    dataset: "breast cancer wisconsin",
    kernel: "rbf",
    C: 10,
    cLog: 1, // log(C) -- use log scale for slider
    gamma: 0.0001,
    gammaLog: -4, // log(gamma) -- use log scale for slider
    coef0: 0.0,
    degree: 3,
    trainSize: 0.7,
    kFolds: null,
    technique: "train-test", // train-test or kFolds
    features: defaultFeatures,
  };
  const [svmParameters, setSvmParameters] = useState<SvmParameters>(
    localStorage.getItem("train-svm")
      ? JSON.parse(localStorage.getItem("train-svm")!)
      : defaultParameters
  );

  // a trigger to re-render the component when the reset button is clicked
  const [reset, setReset] = useState(false);

  // save SVM parameters to local storage
  useEffect(() => {
    localStorage.setItem("train-svm", JSON.stringify(svmParameters));
  }, [svmParameters]);

  // Update list of features when dataset is changed
  useEffect(() => {
    const dataset = svmParameters.dataset;
    const request = {
      dataset_name: dataset,
    };
    console.log(request);
    const getFeatures = async () => {
      try {
        await axios
          .post("http://127.0.0.1:5000/load_data", request)
          .then((response) => {
            // Use the list of features (response.feature_columns) as keys, and set all values to true
            const featuresDictionary = Object.fromEntries(
              response.data.feature_columns.map((feature: string) => [
                feature,
                true,
              ])
            );
            setSvmParameters((prevState) => ({
              ...prevState,
              features: featuresDictionary,
            }));
            console.log("features", featuresDictionary);
          });
      } catch (error) {
        console.error("Error while making the API call:", error);
      }
    };
    getFeatures();
  }, [svmParameters.dataset]);

  useEffect(() => {
    setSvmParameters((prevState) => ({
      ...prevState,
    }));
  }, [reset]);

  // handle change function for select
  const handleSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = event.target;
    if (name === "technique" && value === "kFolds") {
      setSvmParameters((prevState) => ({
        ...prevState,
        technique: value,
        trainSize: null,
        kFolds: 5,
      }));
    } else if (name === "technique" && value === "train-test") {
      setSvmParameters((prevState) => ({
        ...prevState,
        technique: value,
        trainSize: 0.7,
        kFolds: null,
      }));
    } else {
      setSvmParameters((prevState) => ({
        ...prevState,
        [name]: value,
      }));
    }
  };

  // handle change function for input
  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    if (name === "cLog") {
      setSvmParameters((prevState) => ({
        ...prevState,
        C: Math.pow(10, Number(value)),
        cLog: Number(value),
      }));
    } else if (name === "gammaLog") {
      setSvmParameters((prevState) => ({
        ...prevState,
        gamma: Math.pow(10, Number(value)),
        gammaLog: Number(value),
      }));
    } else {
      setSvmParameters((prevState) => ({
        ...prevState,
        [name]: Number(value),
      }));
    }
  };

  // handle reset function
  // set all parameters to default values except for dataset
  const handleReset = () => {
    setSvmParameters((prevState) => ({
      ...defaultParameters,
      dataset: prevState.dataset,
    }));
    setReset((prevTrigger) => !prevTrigger);
    localStorage.removeItem("svm-results");
  };
    
  // handle feature selection changes
  const handleFeatureSelection = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name } = event.target;
    setSvmParameters((prevState) => ({
      ...prevState,
      features: {
        ...prevState.features,
        [name]: !prevState.features[name],
      },
    }));
  };

  // capitalize first letter of each word in string
  const capitalize = (str: string) => {
    return str
      .split(" ")
      .map((word) => word[0].toUpperCase() + word.slice(1))
      .join(" ");
  };

  return (
    <div className="svm-components">
      <div className="train-svm-model-form">
        <Form className="form-svm">
          <Card className="train-svm-model-card">
            <Card.Header>Dataset</Card.Header>
            <Form.Group controlId="formDatasetName">
              <Form.Select
                aria-label="Dataset"
                name="dataset"
                value={svmParameters.dataset}
                onChange={handleSelect}
              >
                {svmDataSetNames.map((datasetName) => (
                  <option key={datasetName} value={datasetName}>
                    {capitalize(datasetName)}
                  </option>
                ))}
              </Form.Select>
            </Form.Group>
          </Card>
          <Card className="train-svm-model-card">
            <Card.Header>Kernel</Card.Header>
            <Form.Group controlId="formKernel">
              <Form.Select
                aria-label="Kernel"
                name="kernel"
                onChange={handleSelect}
                value={svmParameters.kernel}
              >
                <option value="linear">Linear</option>
                <option value="poly">Polynomial</option>
                <option value="rbf">Radial Basis Function</option>
                <option value="sigmoid">Sigmoid</option>
                <option value="precomputed">Precomputed</option>
              </Form.Select>
            </Form.Group>
          </Card>
          <Card className="train-svm-model-card">
            <Card.Header>Hyperparameters</Card.Header>
            <Form.Group className="form-group" controlId="formC">
              <Form.Label>C</Form.Label>
              <Form.Range
                aria-label="C"
                name="cLog"
                min="-2"
                max="5"
                step="0.125"
                onChange={handleInput}
                value={svmParameters.cLog}
              />
              <Form.Text className="text-slider-value">
                {svmParameters.C > 1
                  ? svmParameters.C.toFixed(0)
                  : svmParameters.C.toFixed(2)}
              </Form.Text>
            </Form.Group>
            <Form.Group className="form-group" controlId="formGamma">
              <Form.Label>Gamma</Form.Label>
              <Form.Range
                aria-label="gamma"
                name="gammaLog"
                min="-5"
                max="2"
                step="0.125"
                onChange={handleInput}
                value={svmParameters.gammaLog}
              />
              <Form.Text className="text-slider-value">
                {svmParameters.gamma > 1
                  ? svmParameters.gamma.toFixed(0)
                  : svmParameters.gamma.toFixed(5)}
              </Form.Text>
            </Form.Group>
            <Form.Group className="form-group" controlId="formCoef0">
              <Form.Label>Coef0</Form.Label>
              <Form.Range
                aria-label="coef0"
                name="coef0"
                min="0"
                max="10"
                step="1"
                onChange={handleInput}
                value={svmParameters.coef0}
              />
              <Form.Text className="text-slider-value">
                {svmParameters.coef0.toFixed(1)}
              </Form.Text>
            </Form.Group>
            <Form.Group className="form-group" controlId="formDegree">
              <Form.Label>Degree</Form.Label>
              <Form.Range
                aria-label="degree"
                name="degree"
                min="1"
                max="10"
                step="1"
                onChange={handleInput}
                value={svmParameters.degree}
              />
              <Form.Text className="text-slider-value">
                {svmParameters.degree.toFixed(0)}
              </Form.Text>
            </Form.Group>
          </Card>
          <Card className="train-svm-model-card">
            <Card.Header>Train/Test Technique</Card.Header>
            <Form.Group controlId="formTechnique">
              <Form.Select
                aria-label="Technique"
                name="technique"
                onChange={handleSelect}
                value={svmParameters.technique}
              >
                <option value="train-test">Repeated Subsampling</option>
                <option value="kFolds">K-Fold Cross Validation</option>
              </Form.Select>
            </Form.Group>
            {svmParameters.technique === "kFolds"
              ? svmParameters.kFolds && (
                  <Form.Group className="form-group" controlId="formKfolds">
                    <Form.Label>K-Folds</Form.Label>
                    <Form.Range
                      aria-label="k-folds"
                      name="kFolds"
                      min="2"
                      max="10"
                      step="1"
                      onChange={handleInput}
                      value={svmParameters.kFolds}
                    />
                    <Form.Text className="text-slider-value">
                      {svmParameters.kFolds}
                    </Form.Text>
                  </Form.Group>
                )
              : svmParameters.trainSize && (
                  <Form.Group className="form-group" controlId="formTrainSize">
                    <Form.Label>Train Size</Form.Label>
                    <Form.Range
                      aria-label="train-size"
                      name="trainSize"
                      min="0.01"
                      max="0.99"
                      step="0.01"
                      onChange={handleInput}
                      value={svmParameters.trainSize}
                    />
                    <Form.Text className="text-slider-value">
                      {svmParameters.trainSize.toFixed(2)}
                    </Form.Text>
                  </Form.Group>
                )}
          </Card>
          <div className="button-group">
            <Link to="/learn/supervised/svm/generated-model">
              <Button type="button">Train Model</Button>
            </Link>
            <Button
              variant="secondary"
              type="reset"
              onClick={handleReset}
            >
              Reset Parameters
            </Button>
          </div>
        </Form>
      </div>
      <div className="train-svm-model-feature-selection">
        <Card className="train-svm-model-card">
          <Card.Header>Feature Selection</Card.Header>
          <Card.Body>
            <Form.Group controlId="formFeatureSelection">
              {Object.entries(svmParameters.features).map(
                ([feature, checked]) => (
                  <Form.Check
                    key={feature}
                    id={`${feature}-checkbox`}
                    name={feature}
                    type="checkbox"
                    label={feature}
                    checked={checked}
                    onChange={handleFeatureSelection}
                  />
                )
              )}
            </Form.Group>
          </Card.Body>
        </Card>
      </div>
      <InteractiveHelper section={helperContentText.svm}/>
    </div>
  );
}
