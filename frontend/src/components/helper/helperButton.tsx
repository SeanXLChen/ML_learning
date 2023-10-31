import { AiOutlineQuestion } from "react-icons/ai";

import "../../styles/helper.scss";

interface HelperButtonProps {
    onClick: () => void;
}

export default function HelperButton({onClick}: HelperButtonProps) {
    
    return <button className="helperButton" onClick={onClick}> <AiOutlineQuestion /> </button>;
}