export interface Board {
    id: string;
    title: string;
    description: string;
    // 공개 유무
    status: BoardStatus;
}

// 공개 유무
export enum BoardStatus {
    PUBLIC = "PUBLIC",
    PRIVATE = "PRIVATE"
}