import { BadRequestException, PipeTransform } from "@nestjs/common";
import { BoardStatus } from "../board.model";

export class BoardStatusValidationPipe implements PipeTransform {
    readonly StatusOptions = [
        BoardStatus.PRIVATE,
        BoardStatus.PUBLIC
    ]

    transform(value: any) {
        value = value.toUpperCase();
        
        if (!this.isStatusValid(value)) {
            throw new BadRequestException(`${value} isn't in the status options`);
        }
        return value;
    }

    private isStatusValid(status: any) {
        const index = this.StatusOptions.indexOf(status);
        // 인덱스에 없는 숫자를 넣으면 -1 가 나옴 -> 없는 status 확인!
        return index !== -1;
    }
}