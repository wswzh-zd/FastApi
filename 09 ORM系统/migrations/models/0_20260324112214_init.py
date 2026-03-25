from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `sno` INT NOT NULL COMMENT '学号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '教师名称',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `tno` INT NOT NULL COMMENT '教师编号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL,
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWW1P2zAQ/ison5jEpr637FvphsYYIAGbJgGK3MRJo6Z2cZxBhfLfZztO7aRJltIOAu"
    "qXvtyd7bvH57snzpMxwzb0g08jHwTG570nA4EZZD9S8oM9A8znSsoFFIx9YWglFuOAEmBR"
    "JnOAH0AmsmFgEW9OPYyYFIW+z4XYYoYecpUoRN59CE2KXUgnkDDFzR0Te8iGjzBI/s6npu"
    "NB30656dl8bSE36WIuZCeIHgtDvtrYtLAfzpAyni/oBKOltYcol7oQQQIo5NNTEnL3uXcy"
    "yiSi2FNlEruojbGhA0KfauFWxMDCiOPHvIn3weWrfGw1O/3OoN3rDJiJ8GQp6UdxeCr2eK"
    "BA4PzaiIQeUBBbCBgVbuJ7BbnRBJB86BL7DHjM5Sx4CVRl6CUCBZ9KmVL8jNuw34Y2+4Sg"
    "fxt2Ow3++9BpGNVQnYFH04fIpRP2t90qgfDX8HL0bXi532594HNjltpxvp9LTUuoooinpj"
    "PVQOaCMbCmD4DYZkqj4A9oaEPu1MoWHMmRx6eX0Aci7FXY5eG8imd50R2onMFRkkKJVB4S"
    "ARhu4SLEVlWz1iwrAQi4wmu+Nl8pKVc4JAHMLWSxpryUKZtdMdsVsxcoZoOxA1kBA41xPY"
    "rZgZaNFAKLJbC5VlamB/07O+tRq7aRoCt9YAXJVRiPMYGei07hQqB5wpwCyMrLTVnFrtVM"
    "9UOxqOIzMQEPy3qXyREWJAsN0vjMDq9Gwy9fjai4iW7YPqr04DOAFteYf1bclg0a8f+uvS"
    "WbIpw3M31SC4VwAgLtpYVqjw4mAuwpXGhIyg1dboXUxsOkkk4IDt2JPkpNm5sKTG5m+1lU"
    "SgKSEHJYgBZdMQ0INKMdD6hZmX2fPKB7aLdjBlCP3j9/yEnBYiCleQ1wHFs9xqEGjWY9cA"
    "wQXuMoS+tXZk0Cxh6Dsdt2+hVh3MrBVrDxO6X1eKc2Ykc6U/dyGzLO5AKwfvhVpZtaarwa"
    "19So02ZMU11jvHWiqSLJ8swUMU8zzRSXzBLNNA3dnGkKCMupZvI8lkM1tUe1YqqpPRnuqG"
    "bdiuv7pJq9bveQ9XbYGNTvymlHO7d0dbcW7aR1oZ16avad5otT0Ge9yombyoZvcp7f1t/p"
    "i5whJJ41yeurUlPaVoGy2XXVN9RV/0ASyHNStQdoQ165D1RHMVX9W91uhfLPrArrv9ClGw"
    "A/GmuAKM3fJoDNRqMCgMyqEEChy9xAYETlHXAaxO9XF+cFVxBqSAbIn4gFeGN7Fj3Y872A"
    "3tUT1hIUedTc6VkQ3Ps6ePtnw99ZXEc/Lo4ECjigLhGziAmO1mux228v0V9Njdfd"
)
