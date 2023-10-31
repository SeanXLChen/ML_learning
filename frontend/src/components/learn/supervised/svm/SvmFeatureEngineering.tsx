import InteractiveHelper from "../../../helper/interactiveHelper";
import helperContentText from "../../../../static/helperContentText.json";

export default function SvmFeatureEngineering() {
  return (
    <div>
      <div className="featureEngineering">Feature Engineering</div>
      <InteractiveHelper section={helperContentText.svm}/>
    </div>
  );
}
