import InteractiveHelper from "../../../helper/interactiveHelper";
import helperContentText from "../../../../static/helperContentText.json";
import "../../../../styles/svm.scss";
import hyperplane from "../../../../static/img/hyperplane.webp";
import kernel from "../../../../static/img/SVM-kernal-Equation.webp";
import rbfKernel from "../../../../static/img/RBF-kernel.png";
import ContentRenderer from "../../../root/ContentRenderer";
import staticContent from "../../../../static/staticContent.json";

export default function SvmIntroduction() {
  return (
    <div>
      <ContentRenderer content={staticContent.svmIntroductionPart1} />
      <div className="svm-img">
        <img className="svm-kernel" src={kernel} alt="kernel equation" />
      </div>
      <ContentRenderer content={staticContent.svmIntroductionPart2} />
      <div className="svm-img">
        <img className="svm-rbfKernel" src={rbfKernel} alt="rbfKernel" />
      </div>
      <ContentRenderer content={staticContent.svmIntroductionPart3} />
      <div className="svm-img">
        <img className="svm-hyperplane" src={hyperplane} alt="hyperplane" />
      </div>
      <ContentRenderer content={staticContent.svmIntroductionPart4} />
      <InteractiveHelper section={helperContentText.svm}/>
    </div>
  );
}
