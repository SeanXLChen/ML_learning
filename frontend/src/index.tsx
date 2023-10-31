import React from "react";
import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import AppLayout from "./components/root/AppLayout";
import Home from "./components/root/Home";
import Principles from "./components/background/Principles";
import Glossary from "./components/background/Glossary";
import Eda from "./components/eda/Eda";
import UnderstandingData from "./components/eda/UnderstandingData";
import CleaningData from "./components/eda/ClearningData";
import FeatureEngineering from "./components/eda/FeatureEngineering";
import Learn from "./components/learn/Learn";
import Supervised from "./components/learn/supervised/Supervised";
import SupportVectorMachine from "./components/learn/supervised/SupportVectorMachine";
import SvmIntroduction from "./components/learn/supervised/svm/SvmIntroduction";
import SvmCaseStudy from "./components/learn/supervised/svm/SvmCaseStudy";
import SvmTrainModel from "./components/learn/supervised/svm/SvmTrainModel";
import SvmGeneratedModel from "./components/learn/supervised/svm/SvmGeneratedModel";
import SvmFeatureEngineering from "./components/learn/supervised/svm/SvmFeatureEngineering";
import DecisionTrees from "./components/learn/supervised/DecisionTrees";
import DeepLearning from "./components/learn/deepLearning/DeepLearning";
import Unsupervised from "./components/learn/unsupervised/Unsupervised";
import Reinforcement from "./components/learn/reinforcement/Reinforcement";
import Apply from "./components/apply/Apply";
import Contact from "./components/root/Contact";
import NotFound from "./components/root/NotFound";
import "./index.css";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<Home />} />
          <Route path="background">
            <Route index element={<Principles />} />
            <Route path="glossary" element={<Glossary />} />
          </Route>
          <Route path="eda">
            <Route index element={<Eda />} />
            <Route path="understanding-data" element={<UnderstandingData />} />
            <Route path="cleaning-data" element={<CleaningData />} />
            <Route
              path="feature-engineering"
              element={<FeatureEngineering />}
            />
          </Route>
          <Route path="learn">
            <Route index element={<Learn />} />
            <Route path="supervised">
              <Route index element={<Supervised />} />
              <Route path="svm/" element={<SupportVectorMachine />}>
                <Route index element={<SvmIntroduction />} />
                <Route path="introduction" element={<SvmIntroduction />} />
                <Route path="use-cases" element={<SvmCaseStudy />} />
                <Route path="train-model" element={<SvmTrainModel />} />
                <Route path="generated-model" element={<SvmGeneratedModel />} />
                <Route path="feature-engineering" element={<SvmFeatureEngineering />} />
              </Route>
              <Route path="decision-trees" element={<DecisionTrees />} />
            </Route>
            <Route path="unsupervised" element={<Unsupervised />} />
            <Route path="deep-learning" element={<DeepLearning />} />
            <Route path="reinforcement" element={<Reinforcement />} />
          </Route>
          <Route path="apply" element={<Apply />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
